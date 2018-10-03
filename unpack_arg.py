def health_calculater(age, apples_ate, cigs_smoked):
    answer = (100-age) + (apples_ate * 3.5) - (cigs_smoked * 2)
    print(answer)

dr3as_data = (34, 1, 0)


health_calculater(*dr3as_data)