import numpy as np 

from portfolio_trade.env.custom_env import Portfolio_Prediction_Env


def train_decision(config=None, save=False, calender=None, history=None, all_quotes=None, predict_results_dict=None):
    """
    训练决策模型，从数据库读取数据并进行决策训练

    参数：
        config:配置文件, 
        save：保存结果, 
        calender：交易日日历, 
        history：行情信息, 
        all_quotes:拼接之后的行情信息
        predict_results_dict：预测结果信息
    """



def order_process_trade():
    """
    处理订单（实盘环境）
    """

def connect_vnpy():
    """
    通过vnpy发送订单
    """
