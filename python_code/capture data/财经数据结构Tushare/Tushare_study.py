'''
get_hist_data() 函数可以获取三年内A股历史行情，其他相似功能函数get_h_data()和get_k_data()
'''
# 小例子
import tushare as ts
data=ts.get_hist_data('600848',start='2018-03-01',end='2018-03-08')
print(data)

#小项目任务：利用tushare 包中的接口函数获取招商银行（股票代码600036）2019年第一季度的股票数据并完成如下数据处理和分析任务
# import tushare as ts
# help(ts)
# data=ts.get_hist_data('600036',start='2019-01-01',end='2019-03-31')
# 1 数据只保留date、open、high、close、low和volume 这几个属性，并按时间先后顺序对数据进行排序
# result=data[:,:]
# 2 选择2019年一季度和1月份该股票最高价high和最低价low数据
# result2=data[]



















