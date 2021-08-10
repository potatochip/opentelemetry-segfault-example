## Setup
`brew install k6`


## Test
Run the following commands:

`docker build -t otseg .`

When automatically instrumented under load then segfault occurs (sometimes takes a couple sessions, but almost always occurs on the first try):

`docker run -it -p 8000:8000 --entrypoint scripts/auto otseg`

When manually instrumented under load then no segfault

`docker run -it -p 8000:8000 --entrypoint scripts/manual otseg`

Run load test with `k6 run --vus 100 --iterations 10000 load.js` in a separate terminal
