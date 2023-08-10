# Spark-demo
v3.2.4

# Spark 설치
``` bash
$ wget https://dlcdn.apache.org/spark/spark-3.2.4/spark-3.2.4-bin-hadoop3.2.tgz
$ tar -xvf spark-3.2.4-bin-hadoop3.2.tgz
```

# Container 빌드 과정에서 해야 할 일
1. 환경 변수로 $SPARK_HOME export
2. $SPARK_HOME/conf/spark-defaults.conf.template 파일을 spark-defaults.conf 로 copy
3. spark-defaults.conf 파일 설정 (Master, Serealizer 주석 해제 필수)