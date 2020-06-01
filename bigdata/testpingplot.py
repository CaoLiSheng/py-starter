# -*- coding: utf-8 -*-

import datetime
import subprocess
import os
import re
import time


def get_ping_result(ip_address):
    pipe_stream = subprocess.Popen(
        ['ping', ip_address],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True
    )

    stream_out = pipe_stream.stdout.read().decode('utf-8')
    print(stream_out)
    pack_receive = re.search('已接收 = \d', stream_out)
    receive_count = int(pack_receive.group()[6:])

    if receive_count:
        pack_send = re.search('已发送 = \d', stream_out)
        send_count = pack_send.group()[6:]
        reg_max_time = '最长 = \d+ms'
        reg_min_time = '最短 = \d+ms'
        reg_avg_time = '平均 = \d+ms'
        max_time = re.search(reg_max_time, stream_out).group()[5:-2]
        min_time = re.search(reg_min_time, stream_out).group()[5:-2]
        avg_time = re.search(reg_avg_time, stream_out).group()[5:-2]
        return [max_time, min_time, avg_time, receive_count, send_count]
    else:
        return False


if __name__ == '__main__':
    dir_name = 'logs'
    file_name = (time.strftime(
        '%Y-%m-%d', time.localtime(time.time()))) + '.log'
    if os.path.exists(dir_name) is False:
        os.mkdir(dir_name)
    file_path = os.getcwd()+'\\'+dir_name+'\\'+file_name

    ip_list = [
        ['核心交换', '172.16.254.1'],
        ['公司外网', '116.53.170.137'],
        ['电信网关', '116.53.170.1'],
        ['PACS', '192.168.10.10'],
        ['HIS', '192.168.0.253'],
        ['LIS', '192.168.0.200'],
        ['电子病历', '192.168.0.10'],
        ['防火墙', '10.0.100.253'],
        ['EDR', '192.168.0.251'],
        ['文件服务器', '192.168.0.250']
    ]

    while True:
        with open(file_path, 'a') as log_t:
            for item_i in ip_list:
                ping_result = get_ping_result(item_i[1])
                nowTime = datetime.datetime.now().strftime('%H:%M:%S')
                if ping_result:
                    max_time = str(ping_result[0])
                    min_time = str(ping_result[1])
                    avg_time = str(ping_result[2])
                    send_count = str(ping_result[3])
                    receive_count = str(ping_result[4])
                    log = (nowTime + ' ' + item_i[0] + ':' + item_i[1] + ' '
                           + '已发送:' + send_count + ' ' + '已接收:' + receive_count + ' '
                           + '最长:' + max_time + ' ' + '最短:' + min_time + ' ' + '平均:' + avg_time + ' ')
                    print(log)
                    log_t.write(log + '\n')
                else:
                    log = (nowTime + ' ' + item_i[0] + ':' + item_i[1] + ' '
                           + '已发送:4 已接收:0' + ' ' + '请求超时')
                    print(log)
                    log_t.write(log + '\n')
            print()
            log_t.write('\n')
