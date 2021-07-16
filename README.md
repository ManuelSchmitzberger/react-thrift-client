# React Thrift Client Demo

### This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app)
```
npx create-react-app react-thrift-client
```

### Install packages
```
npm install --save @creditkarma/thrift-client @creditkarma/thrift-server-core typescript @types/node @types/react @types/react-dom @types/jest
npm install --save-dev @creditkarma/thrift-typescript
```

### Modify package.json
Add a script in `package.json`:
```
"codegen": "thrift-typescript --target thrift-server --sourceDir thrift --outDir src/codegen"
```

### Thrift IDL
The Thrift IDL file locates in the `thrift` folder.
* The demo IDL has a `getUserInfo` method which returns users name and email.

### Codegen
```sh
$ ./generate-thrift.sh
```
It will read the IDL in `./thrift` and create Thrift related files in `./src/codegen` for the client.
The server files are located in `./thrift/gen-py`

### Server setup

* Python

```sh
$ python -m venv venv
$ . ./venv/bin/activate
$ pip install -r requirements.txt
```

Start the server:

```sh
$ python server.py
```

* Go

```sh
$ cd server/go
$ go install
$ go run ./server.go
```


### Start the client

```sh
$ yarn start
```
Visit `localhost:3000`


### Run browser

run google-chrome without CORS check.

```sh
google-chrome-unstable --disable-web-security --user-data-dir="/tmp"
```
