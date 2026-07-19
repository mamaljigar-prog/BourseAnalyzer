# growth_model.py


def sales_growth(
        current_sales,
        previous_sales
):

    if previous_sales == 0:
        return 0


    growth = (
        (current_sales - previous_sales)
        /
        previous_sales
    ) * 100


    return round(
        growth,
        2
    )



def average_growth(
        growth_list
):

    if not growth_list:
        return 0


    return round(
        sum(growth_list)
        /
        len(growth_list),
        2
    )



if __name__ == "__main__":


    # تست خراسان

    current = 143134988

    previous = 120000000


    result = sales_growth(
        current,
        previous
    )


    print("================")
    print("رشد فروش")
    print("================")

    print(
        result,
        "%"
    )