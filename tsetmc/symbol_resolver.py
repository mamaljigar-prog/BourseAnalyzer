import requests
import unicodedata


class SymbolResolver:

    def __init__(self):

        self.base_url = (
            "https://cdn.tsetmc.com/api"
        )

        self.headers = {
            "User-Agent": "Mozilla/5.0"
        }


    def _normalize_symbol(self, value):

        if value is None:
            return ""

        value = str(value)

        # Normalize Unicode
        value = unicodedata.normalize(
            "NFKC",
            value
        )

        # Arabic/Persian character normalization
        value = value.replace(
            "ي",
            "ی"
        )

        value = value.replace(
            "ى",
            "ی"
        )

        value = value.replace(
            "ك",
            "ک"
        )

        # Remove zero-width characters
        value = value.replace(
            "\u200c",
            ""
        )

        value = value.replace(
            "\u200d",
            ""
        )

        value = value.replace(
            "\ufeff",
            ""
        )

        # Remove whitespace
        value = "".join(
            value.split()
        )

        return value.strip()


    def find_ins_code(
        self,
        symbol
    ):

        original_symbol = symbol

        normalized_symbol = (
            self._normalize_symbol(
                symbol
            )
        )


        url = (
            f"{self.base_url}/Instrument/"
            "GetInstrumentSearch/"
            f"{symbol}"
        )


        response = requests.get(

            url,

            headers=self.headers,

            timeout=15

        )


        response.raise_for_status()


        data = response.json()


        if isinstance(
            data,
            dict
        ):

            items = (

                data.get(
                    "instrumentSearch"
                )

                or

                data.get(
                    "instrumentSearchList"
                )

                or

                []

            )

        else:

            items = data


        if not isinstance(
            items,
            list
        ):

            return None


        # ==========================================
        # Exact normalized match
        # ==========================================

        for item in items:

            if not isinstance(
                item,
                dict
            ):

                continue


            names = [

                item.get(
                    "lVal18AFC"
                ),

                item.get(
                    "symbol"
                ),

                item.get(
                    "lVal18"
                ),

                item.get(
                    "name"
                )

            ]


            for name in names:

                normalized_name = (

                    self._normalize_symbol(
                        name
                    )

                )


                if (

                    normalized_name

                    ==

                    normalized_symbol

                ):

                    return (

                        item.get(
                            "insCode"
                        )

                        or

                        item.get(
                            "inscode"
                        )

                    )


        # ==========================================
        # Fallback:
        # API may return the requested symbol
        # with a minor Unicode/format difference.
        # ==========================================

        for item in items:

            if not isinstance(
                item,
                dict
            ):

                continue


            candidate_code = (

                item.get(
                    "insCode"
                )

                or

                item.get(
                    "inscode"
                )

            )


            if not candidate_code:

                continue


            candidate_names = [

                item.get(
                    "lVal18AFC"
                ),

                item.get(
                    "symbol"
                ),

                item.get(
                    "lVal18"
                ),

                item.get(
                    "name"
                )

            ]


            for name in candidate_names:

                if not name:

                    continue


                normalized_name = (

                    self._normalize_symbol(
                        name
                    )

                )


                if (

                    normalized_symbol
                    in
                    normalized_name

                    or

                    normalized_name
                    in
                    normalized_symbol

                ):

                    return candidate_code


        return None