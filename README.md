gae-ci-test-app
===============


![Build status](https://www.codeship.io/projects/e2c75c10-4dfe-0131-8641-0a8b93fd95bc/status)
[![Build Status](https://drone.io/github.com/akiray03/gae-ci-test-app/status.png)](https://drone.io/github.com/akiray03/gae-ci-test-app/latest)

test (js)
---------

```bash
$ phantomjs run-qunit.js js/test/test.html

  or

$ phantomjs run-qunit.js js/test/test.html | egrep '<|>' > junit-report.xml
```

test (python)
-------------

```bash
$ python test/rungaetest.py <PATH-TO-GAE-SDK> ./test/
```
