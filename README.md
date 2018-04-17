serverless-aws-py
=================

This repo holds a basic template to deploy python codes to AWS lambda function.

## 1. Setup
#### AWS policy for serverless bot
Please create an IAM bot-user in AWS. A default policy for Singapore region can be found in `serverless-aws-py-dev-ap-southeast-1-policy.json`. You can also generate your own policy with yeoman:
```bash
npm run policy
```

#### Setup AWS credentials locally
Please ensure your AWS credentials are exported as your current environment variables `AWS_KEY` and `AWS_SECRET` respectively. Otherwise you can create an `.env` file of the form:

> AWS_KEY=SOMERANDOMIDKEY  
> AWS_SECRET=SOMERANDOMSECRETVALUE

Run the following command once to setup your credentials:
```bash
npm run init
```

## 2. Usage

#### Setup nodeJS dependencies
```bash
npm i
```
or
```bash
yarn
```

#### Deploy all functions to AWS
```bash
npm run deploy
```

#### Deploy specific function to AWS
```bash
npm run deployf -- <name of the function>
```

#### Remove all and clean functions from AWS
```bash
npm run remove
```

#### Test locally
```bash
npm run function -- <name of the function>
npm run function -- echo --data hello!
```

#### Test deployed function
```bash
npm run api -- <name of the function>
npm run api -- echo --data hello!
```

#### Test api endpoint
You will see the api endpoint after deploying to AWS
> curl -d [DATA] -X POST [API_ENDPOINT]

```bash
# example
curl -d "hello!" -X POST https://abcdef.execute-api.ap-southeast-1.amazonaws.com/dev/echo
```

#### Others
Please look at [serverless cli documentation](https://serverless.com/framework/docs/providers/aws/cli-reference/) for more details.

As `serverless` is installed locally, please prefix the command with a `npx`:
```bash
npx serverless
```
