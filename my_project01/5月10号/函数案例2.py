def cal(*object, coupon, score, delivery):
    """
    根据传入的商品、优惠券、积分、运费计算订单总金额
    :param object: 商品信息，名称、价格、数量
    :param coupon: 优惠券
    :param score: 积分
    :param delivery: 运费
    :return: 总金额
    """
    #订单总金额 = 商品价格 - 优惠券 - 积分 + 运费
    #1. 商品总金额
    total_price = [s[1]*s[2] for s in object]
    total_cost = sum(total_price)
    #2. 优惠券
    if total_cost >= 5000 and coupon <= total_cost:
        total_cost -= coupon
    #3. 积分
    if total_cost >= 5000 and score//100 <= total_cost:
        total_cost -= score//10010
        

    #4.运费
    total_cost += delivery
    return total_cost

cost = cal(("1",188,2),("2",999,1),("3",546,6),("4",900,1),coupon=10,score=900,delivery=10)
print(cost)