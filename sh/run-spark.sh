#!/bin/bash

# 실행 커맨드 = sh run-spark.sh $SPARK_HOME

# SPARK_HOME 디렉토리 가져오기
SPARK_HOME=$1

# master 실행
$SPARK_HOME/sbin/start-master.sh

# worker 실행
# master 호스트 주소 설정 : 환경 변수 조정
$SPARK_HOME/sbin/start-worker.sh \
spark://neivekim76.local:7077 \
-m 3g