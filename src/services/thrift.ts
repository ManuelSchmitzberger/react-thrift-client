/* eslint-disable import/named */
import {
  DemoService
} from '../codegen/com/demo';

import { createHttpClient } from '@creditkarma/thrift-client';

const runHello = () => {
  const clientConfig = {
    hostName: 'localhost',
    port: 9090,
    requestOptions: {} // CoreOptions to pass to Request
    //path: '/',
  };

  const demoClient: DemoService.Client = createHttpClient(DemoService.Client, clientConfig);

  return new Promise((resolve, reject) => {
    demoClient.hello().then(() => {
      resolve();
    }, (err: unknown) => {
      reject(err);
    });
  });
};

export { runHello };
