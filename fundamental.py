class FundamentalScore:


    def __init__(
        self,
        current,
        previous,
        quality_score,
        pe_normalized,
        pe_forward
    ):

        self.current = current
        self.previous = previous
        self.quality_score = quality_score
        self.pe_normalized = pe_normalized
        self.pe_forward = pe_forward



    def growth_score(
        self,
        current_value,
        previous_value,
        max_score
    ):


        if previous_value == 0:

            return 0



        growth = (
            (current_value - previous_value)
            /
            previous_value
        ) * 100



        if growth >= 30:

            return max_score


        elif growth >= 15:

            return max_score * 0.7


        elif growth > 0:

            return max_score * 0.4


        else:

            return 0




    def valuation_score(self):

        score = 0



        if self.pe_normalized < 7:

            score = 10


        elif self.pe_normalized < 10:

            score = 7


        elif self.pe_normalized < 15:

            score = 4


        else:

            score = 1



        return score





    def quality_score_value(self):

        return (
            self.quality_score / 10
        ) * 20





    def risk_penalty(self):

        penalty = 0



        # کیفیت سود ضعیف

        if self.quality_score < 7:

            penalty += 10



        # P/E نرمال بالا

        if self.pe_normalized > 15:

            penalty += 5



        # فاصله زیاد P/E خام و نرمال

        if (
            self.pe_normalized
            >
            self.pe_forward * 1.5
        ):

            penalty += 5



        return penalty





    def calculate(self):


        score = 0



        # رشد فروش

        score += self.growth_score(

            self.current.sales,

            self.previous.sales,

            25

        )



        # رشد سود عملیاتی

        score += self.growth_score(

            self.current.operating_profit,

            self.previous.operating_profit,

            25

        )



        # رشد سود خالص

        score += self.growth_score(

            self.current.net_profit,

            self.previous.net_profit,

            20

        )



        # کیفیت سود

        score += self.quality_score_value()



        # ارزش گذاری

        score += self.valuation_score()



        # کسر ریسک

        score -= self.risk_penalty()



        if score < 0:

            score = 0



        if score > 100:

            score = 100



        return round(score)