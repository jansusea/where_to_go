from django.shortcuts import render
from django.db import connection


def index(request):
    return render(request, 'app/index.html')


def demo(request):
    return render(request, 'app/demo.html')


def home(request):
    return render(request, 'app/home.html')


def analysis(request):
    return render(request, 'app/analysis.html')


def house(request):
    # price avgPrice address address1
    # from wherego import models
    # total = models.Item.objects.all().count()
    # print('--------' + str(total))
    # context = {'total': total}
    # return render(request, 'app/show.html', context)
    cursor = connection.cursor()
    # Object of type 'datetime' is not JSON serializable ,用to_char轉換
    # ORA-00911: invalid character ,去掉分號
    # select count(*) from item
    sql = "select avgPrice,address1 from lianjia_transaction order by address1 desc"
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    # tuple tuple 0 1 2 3 4

    house_list = []

    all_count = len(result)
    item_city = result[0][1]
    # init_avg_salary = result[0][4]
    city_all_avg_house_price = 0
    city_house_count = 0
    city_count = 1
    for i in range(len(result)):
        city_house_item = result[i]
        if i != (all_count - 1) and item_city == city_house_item[1]:
            # 如果是同一个城市
            city_house_count += 1
            city_all_avg_house_price += city_house_item[0]
        elif i != (all_count - 1):
            # 如果不是同一个城市，且不是最后一个数
            city_count += 1
            temp_city_avg_house_price = city_all_avg_house_price / city_house_count
            # 需要增加标准差之类统计数据
            house_list.append({
                'city': item_city,
                'city_house_count': city_house_count,
                'city_all_avg_house_price': format(temp_city_avg_house_price, ".2f"),
            })
            # 重新初始化迭代城市名和城市工作数以及城市平均薪水的和
            item_city = city_house_item[1]
            city_house_count = 1
            city_all_avg_house_price = city_house_item[0]
        else:
            # 如果是最后一个数
            if item_city == city_house_item[1]:
                # 如果是相同城市
                city_house_count += 1
                city_all_avg_house_price += city_house_item[0]
            else:
                # 如果不是相同城市

                # 需要把上面一条数据提交
                temp_city_avg_house_price = city_all_avg_house_price / city_house_count
                # 需要增加标准差之类统计数据
                house_list.append({
                    'city': item_city,
                    'city_house_count': city_house_count,
                    'city_all_avg_house_price': format(temp_city_avg_house_price, ".2f"),
                })
                city_count += 1
                item_city = city_house_item[1]
                city_house_count = 1
                city_all_avg_house_price = city_house_item[0]

            # 把最后一条数据记录上去
            temp_city_avg_house_price = city_all_avg_house_price / city_house_count
            # 需要增加标准差之类统计数据
            house_list.append({
                'city': item_city,
                'city_house_count': city_house_count,
                'city_all_avg_house_price': format(temp_city_avg_house_price, ".2f"),
            })
            item_city = city_house_item[1]

    print(house_list)

    context = {'house_list': house_list}
    return render(request, 'app/house.html', context)


def work(request):
    # return render(request, 'app/work.html')
    # from wherego import models
    # total = models.Item.objects.all().count()
    # print('--------' + str(total))
    # context = {'total': total}
    # return render(request, 'app/show.html', context)
    cursor = connection.cursor()
    # Object of type 'datetime' is not JSON serializable ,用to_char轉換
    # ORA-00911: invalid character ,去掉分號
    # select count(*) from item
    sql = "select workingexp,edulevel,city,salary,avgsalary from item order by city desc"
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    # tuple tuple 0 1 2 3 4

    work_list = []

    all_count = len(result)
    item_city = result[0][2]
    # init_avg_salary = result[0][4]
    city_all_avg_salary = 0
    city_work_count = 0
    city_count = 1
    for i in range(len(result)):
        work_item = result[i]
        if i != (all_count - 1) and item_city == work_item[2]:
            # 如果是同一个城市
            city_work_count += 1
            city_all_avg_salary += work_item[4]
        elif i != (all_count - 1):
            # 如果不是同一个城市，且不是最后一个数
            city_count += 1
            temp_city_avg_salary = city_all_avg_salary / city_work_count
            # 需要增加标准差之类统计数据
            work_list.append({
                'city': item_city,
                'city_work_count': city_work_count,
                'city_avg_salary': format(temp_city_avg_salary, ".2f"),
            })
            # 重新初始化迭代城市名和城市工作数以及城市平均薪水的和
            item_city = work_item[2]
            city_work_count = 1
            city_all_avg_salary = work_item[4]
        else:
            # 如果是最后一个数
            if item_city == work_item[2]:
                # 如果是相同城市
                city_work_count += 1
                city_all_avg_salary += work_item[4]
            else:
                # 如果不是相同城市

                # 需要把上面一条数据提交
                temp_city_avg_salary = city_all_avg_salary / city_work_count
                # 需要增加标准差之类统计数据
                work_list.append({
                    'city': item_city,
                    'city_work_count': city_work_count,
                    'city_avg_salary': format(temp_city_avg_salary, ".2f"),
                })
                city_count += 1
                item_city = work_item[2]
                city_work_count = 1
                city_all_avg_salary = work_item[4]

            # 把最后一条数据记录上去
            temp_city_avg_salary = city_all_avg_salary / city_work_count
            # 需要增加标准差之类统计数据
            work_list.append({
                'city': item_city,
                'city_work_count': city_work_count,
                'city_avg_salary': format(temp_city_avg_salary, ".2f"),
            })
            item_city = work_item[2]

    print(work_list)

    context = {'work_list': work_list}
    return render(request, 'app/work.html', context)


def test(request):
    return render(request, 'app/test.html')


def show(request):

    # price avgPrice address address1
    # from wherego import models
    # total = models.Item.objects.all().count()
    # print('--------' + str(total))
    # context = {'total': total}
    # return render(request, 'app/show.html', context)
    cursor = connection.cursor()
    # Object of type 'datetime' is not JSON serializable ,用to_char轉換
    # ORA-00911: invalid character ,去掉分號
    # select count(*) from item
    sql = "select avgPrice,address1 from lianjia_transaction order by address1 desc"
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    # tuple tuple 0 1 2 3 4

    house_list = []

    all_count = len(result)
    item_city = result[0][1]
    # init_avg_salary = result[0][4]
    city_all_avg_house_price = 0
    city_house_count = 0
    city_count = 1
    for i in range(len(result)):
        city_house_item = result[i]
        if i != (all_count - 1) and item_city == city_house_item[1]:
            # 如果是同一个城市
            city_house_count += 1
            city_all_avg_house_price += city_house_item[0]
        elif i != (all_count - 1):
            # 如果不是同一个城市，且不是最后一个数
            city_count += 1
            temp_city_avg_house_price = city_all_avg_house_price / city_house_count
            # 需要增加标准差之类统计数据
            house_list.append({
                'city': item_city,
                'city_house_count': city_house_count,
                'city_all_avg_house_price': format(temp_city_avg_house_price, ".2f"),
            })
            # 重新初始化迭代城市名和城市工作数以及城市平均薪水的和
            item_city = city_house_item[1]
            city_house_count = 1
            city_all_avg_house_price = city_house_item[0]
        else:
            # 如果是最后一个数
            if item_city == city_house_item[1]:
                # 如果是相同城市
                city_house_count += 1
                city_all_avg_house_price += city_house_item[0]
            else:
                # 如果不是相同城市

                # 需要把上面一条数据提交
                temp_city_avg_house_price = city_all_avg_house_price / city_house_count
                # 需要增加标准差之类统计数据
                house_list.append({
                    'city': item_city,
                    'city_house_count': city_house_count,
                    'city_all_avg_house_price': format(temp_city_avg_house_price, ".2f"),
                })
                city_count += 1
                item_city = city_house_item[1]
                city_house_count = 1
                city_all_avg_house_price = city_house_item[0]

            # 把最后一条数据记录上去
            temp_city_avg_house_price = city_all_avg_house_price / city_house_count
            # 需要增加标准差之类统计数据
            house_list.append({
                'city': item_city,
                'city_house_count': city_house_count,
                'city_all_avg_house_price': format(temp_city_avg_house_price, ".2f"),
            })
            item_city = city_house_item[1]

    print(house_list)

    context = {'house_list': house_list}
    return render(request, 'app/show.html', context)


