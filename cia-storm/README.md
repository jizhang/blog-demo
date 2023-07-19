# Clojure In Action - Storm

An example of using Storm to do realtime data processing.

## Usage

Install [Leiningen 2][1] first.

### Run Locally

```bash
$ lein run -m cia-storm.wordcount
```

### Submit to Cluster

```bash
$ lein do clean, compile, uberjar
$ storm jar target/cia-storm-0.1.0-SNAPSHOT-standalone.jar cia_storm.wordcount wordcount
```

## License

Copyright © 2013 FIXME

Distributed under the Eclipse Public License, the same as Clojure.

[1]: https://github.com/technomancy/leiningen
