## Google Cloud Platform (GCP) 세팅



계정만들기

VM 인스턴스 생성하기 - cpu, gpu 둘 다 했음  

gpu 신청하기 - 승인됨  

- 참조사항

  코인 300달러 다 썼을 때 -> 계정 새로 만들고 (ex.lsh9382_2@gmail.com) 이 계정에서 프로젝트 권한 추가를 본 메일(lsh9382@gmail.com) 으로 할 것 -> lsh9382@gmail.com 계정에서 lsh9382_2@gmail.com에서 생성한 인스턴스에 접근할 수 있다.   



## SSH 접속 환경 세팅

### Putty로 key 생성하고 GCP의 메타데이터에 등록하기  

했음   



### SSH key 접속 명령어  

cpu instance와 gpu instance 동일하게 적용됨, 외부 IP 만 바꿔서 접속해 주면 됨  

```
ssh -L 9999:localhost:9999 -i C:\.ssh\rsa-gcp-key -o ServerAliveInterval=15 -o ServerAliveCountMax=3 lsh9382@[vm 인스턴스의 외부 IP]
```



### SSH Host 등록

#### 1. config 파일 열기 

``` 
vim ~/.ssh/config
```

i를 눌러 편집 모드로 전환

#### 2. Host 등록하기 -> private key 해결 아직 안됐음  

[참조](<https://stackoverflow.com/questions/49528663/gcp-vms-ssh-config-file>)   

```
Host gcp1
        HostName [vm 인스턴스의 외부 IP]  
        User lsh9382
        PubkeyAuthentication yes
        IdentityFile C:\.ssh/rsa-gcp-key
```

#### 3. 접속

```
ssh gcp1
```



## Docker 세팅 및 사용 

cpu instance - kubig wiki 보고 했음

gpu instance - kubig wiki 보고 했음  

- 참조할만한 명령어

  Docker 진입한 다음 

  1. cpu 서버의 경우

     ```
     htop
     ```

  2. gpu  서버의 경우 

     ```
     watch -n 1 nvidia-smi
     ```

     

- Docker 접속

  1. cpu 서버의 경우  

     ```
     sudo docker run -it -p 9999:9999 -v ~:/home hyeon95y/kubig:cpu
     ```

     

  2. gpu 서버의 경우  

     다음 명령어 이용해서 Run Docker Image    

     해당 서버의 home directory의 위치가 docker와 mount되는 것임. (포인터 개념)   

     mount 시켜주지 않으면 도커에서 아무리 작업해도 다 날라감. 

     ```
     sudo docker run --runtime=nvidia -it --rm -p 9999:9999 -v ~:/home hyeon95y/kubig:gpu10.1
     ```

     Docker에서 빠져나오려면 __Ctrl + D__   

      


## GPU 서버 내 파이썬 환경 세팅

- Jupyter lab 사용가능한 환경 만들기    

  

  pip 설치 명령어

  ```
  sudo apt install python-pip
  ```

  [참조](<https://quiet-time.tistory.com/64>)  

  config파일생성해서 c.NotebookApp 이거 또 해줘야함.. (옛날에 했던거)   

  

- 데이터 코드, 백테스팅, 트레이딩 전략(ex. WANN)  



## ETC

- 파일 보내는 명령어 __rsync__   

  변한 부분만 복사해주는 명령어  

  [참조](<https://twpower.github.io/153-copy-files-using-rsync-command>)      

  ```
  rsync  
  ```

  