## Google Cloud Platform (GCP) 세팅

계정만들기

VM 인스턴스 생성하기

gpu 신청하기



## SSH 접속 환경 세팅

### Putty로 key 생성하고 GCP의 메타데이터에 등록하기  

했음 



### SSH key 접속 명령어

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



## Docker 세팅 

