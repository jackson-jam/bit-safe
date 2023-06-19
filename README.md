﻿# bit-safe     ——多功能安全webapp
##一、背景
态势感知是一种基于环境的、动态、整体地洞悉安全风险的能力，是从全局视角提升对安全威胁的发现识别、理解分析、响应处置的一种方式,目前态势感知已经成为社会网络安全的主要防护设施，基于这个大环境我们使用自己记录的数据集开发了态势感知系统并整合了各类安全工具，为用户提供一个全面的高可用性的系统。


##二、功能
###2.1态势感知
我们的态势感知系统是基于机器学习构建的模型，主要分为：
①对实时数据包的嗅探
实现：
使用Scapy进行实时数据包嗅探，并将嗅探结果以json格式传给前端
②对攻击数据包分析并对态势感知的分类模型
实现：
利用numpy、pandas库与sklearn工具集对攻击数据包进行嗅探分析
先进行数据预处理：按列归一化（zero-score）利用数据回归算法与逻辑回归算法对数据进行整理，使用决策树算法进行模型预测，随机森林进行分类与回归。使用sklearn工具切分数据集，测试集为原数据集的30%。再用model进行模型训练及评估，最后通过对大量攻击数据包的感知与分析来训练模型.用训练模型来判断攻击类型并应对。


此外，我们还加入了额外的规则限定，我们在机器学习的入侵检测模型上集成了静态的规则检测模型，用于自定义白名单或者黑名单。


###2.2漏洞扫描
漏洞扫描是指基于漏洞数据库，通过扫描等手段对指定的远程或者本地计算机系统的安全脆弱性进行检测，发现可利用漏洞的一种安全检测的行为。
我们利用python开发了我们自己的web漏洞扫描器，并且加入了AWVS的接口，两个扫描同时进行，我们的程序可以通过对两个扫描结果的汇总，结合了前端的UI设计，以简洁明了的图表形式展示，还有更详细的日志信息等，并且可以再扫描完成后导出报告，让用户能够更快速的了解到最准确的漏洞扫描结果。


##三、环境部署
该工具是基于python的django框架搭建的，整个项目的源码全部为团队成员完成，在项目的初期只能通过源码来部署，而现在我们已经成功的利用docker容器完成一键部署，只需要更改用户dockerfile的配置利用简单两句命令即可实现部署。
