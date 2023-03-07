# Formal Models of Signal with the session-handling layer Sesame and clone detection

This folder accompanies the paper [Formal Analysis of Session-Handling in Secure Messaging: Lifting Security from Sessions to Conversations](https://eprint.iacr.org/2022/1710) by [Cas Cremers](https://people.cispa.io/cas.cremers), [Charlie Jacomme](https://charlie.jacomme.fr), and [Aurora Naska](https://cispa.de/en/people/aurora.naska); it contains the needed materials to reproduce our case-studies.

The folder `Sesame` contains the actual models, with a dedicated README. The models are created for the theorem prover [Tamarin prover](https://tamarin-prover.github.io/).

## Using docker

We provide via dockerhub an anonymous docker with the required presintalled version of Tamarin.

The image can be fetched via:
```
$ docker pull sesameproof/tamarin
```

Then, from this repository, or one that has the `Sesame` inside of it, one should run:
```
 $ docker run -it -v $PWD:/opt/case-studies sesameproof/tamarin bash
```

This should give you a shell, where the commands `tamarin-prover` can be executed, and the README inside the `Sesame` folder followed.

## Compiling the tools from scratch

We provide in this folder the `tamarin-prover.zip` containing the source files for [Tamarin prover](https://tamarin-prover.github.io/), with installation instructions at [https://tamarin-prover.github.io/manual/book/002_installation.html].
