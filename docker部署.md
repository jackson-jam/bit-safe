docker 部署（1）

首先从github上拉取我们的代码

然后到mysite目录下

![截屏2023-05-22 11.19.16](/Users/shiwu/Library/Application Support/typora-user-images/截屏2023-05-22 11.19.16.png)

然后在此目录下使用命令

```docker build -t bitsafe . ```

即可构建docker镜像  ![截屏2023-05-22 11.20.44](/Users/shiwu/Library/Application Support/typora-user-images/截屏2023-05-22 11.20.44.png)

此时使用命令

```docker images```

即可看到我们新建的镜像

![截屏2023-05-22 11.21.43](/Users/shiwu/Library/Application Support/typora-user-images/截屏2023-05-22 11.21.43.png)

再使用命令

```docker run -p 8000:8000 --name bitsafe-v1.0 bitsafe ```

会出现如下界面

![截屏2023-05-22 11.23.30](/Users/shiwu/Library/Application Support/typora-user-images/截屏2023-05-22 11.23.30.png)

此时访问127.0.0.1:8000即可查看到我们的项目

![截屏2023-05-22 11.24.42](/Users/shiwu/Library/Application Support/typora-user-images/截屏2023-05-22 11.24.42.png)