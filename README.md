gae-ci-test-app
===============

[![Build Status](https://drone.io/github.com/akiray03/gae-ci-test-app/status.png)](https://drone.io/github.com/akiray03/gae-ci-test-app/latest)

[![Build Status](https://www.codeship.io/projects/7c347860-4e10-0131-3cc0-3a304a73959b/status)](https://www.codeship.io/projects/11307)

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
