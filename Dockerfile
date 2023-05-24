FROM python:3.9.0
LABEL authors="cangxueqifeng"


WORKDIR /mysite/
ENV DB_NAME=hpxh
ENV DB_USER=root
ENV DB_PASSWORD=jujingyi
ENV DB_HOST=host.docker.internal
ENV DB_PORT=3306
#使用这个本地的时候可以
#COPY pip.conf /root/.pip/pip.conf
COPY requirements.txt requirement.txt
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
CMD ["python", "manage.py", "runserver","0.0.0.0:8000"]
#ENTRYPOINT ["top", "-b"]