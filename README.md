This folder contains the needed material to reproduce our case-studies.

The folder `Sesame` contains the actual models, with a dedicated README.

# Using docker

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

# Compiling the tools from scratch

We provide in this folder the `tamarin-prover.zip` containing the source files for Tamarin, with installation instructions at [https://tamarin-prover.github.io/manual/book/002_installation.html].
