>  **gvp-backend** 采集平台FastApi后端项目

## 环境
    python 3.9.7

## 开发

    1：准备python运行环境,安装requirements.txt依赖.
    2：在core/settings.py文件中修改配置
    3：运行main.py

## 调试
    http://localhost:60002/docs 访问swagger接口调试界面

## 单元测试
    /test目录下保存所有接口的测试用例, 终端运行pytest执行测试, 测试前需保证测试数据库的表都为空.
