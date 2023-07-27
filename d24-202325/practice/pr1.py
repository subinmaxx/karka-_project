jewel=[
        {
            "month":"january",
            "gold_rate":1500,
            "jewel_list":[{"name":"chain","making_cost":10},
                          {"name":"ring","making_cost":15}
                         ]
        },
        {
          "month":"february",
            "gold_rate":1600,
            "jewel_list":[{"name":"chain","making_cost":12},
                          {"name":"ring","making_cost":16}                          
                         ]
        },
        {
            "month":"march",
            "gold_rate":2000,
            "jewel_list":[{"name":"chain","making_cost":16},
                          {"name":"ring","making_cost":18}
                         ]
        }
    ]
for i in jewel:
    price=i["gold_rate"]
    for value in i["jewel_list"]:
        making=value["making_cost"]
        amount=price*making/100
        # print(amount)
        total_amount=price+amount
        print(total_amount)