### 项目名称

探索美国共享单车数据

### 简介

利用 Python 探索与以下三大美国城市的自行车共享系统相关的数据：芝加哥、纽约和华盛顿特区。编写python脚本实现交互式体验，以展现这些统计信息。

### 数据来源

原始文件访问地址：([芝加哥](https://www.divvybikes.com/system-data)、[纽约市](https://www.citibikenyc.com/system-data)、[华盛顿特区](https://www.capitalbikeshare.com/system-data)）

数据压缩为了核心**六 (6)** 列：

- 起始时间 Start Time（例如 2017-01-01 00:07:57）
- 结束时间 End Time（例如 2017-01-01 00:20:53）
- 骑行时长 Trip Duration（例如 776 秒）
- 起始车站 Start Station（例如百老汇街和巴里大道）
- 结束车站 End Station（例如塞奇威克街和北大道）
- 用户类型 User Type（订阅者 Subscriber/Registered 或客户Customer/Casual）

### 参考

1.[项目练习答案3](https://classroom.udacity.com/nanodegrees/nd002-cn-basic/parts/ce2f97bf-7be1-4142-a764-9b59ec87985f/modules/c4200d90-6104-4463-8e72-2d462feaaca1/lessons/0e6ec8f1-fcb5-4374-b50e-eb44eca45a1c/concepts/b05491a6-fd04-4889-8736-df78744b3615)

2.[pandas关于获取星期的文档](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.dt.day_name.html)