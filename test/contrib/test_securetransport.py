# -*- coding: utf-8 -*-
import pytest

try:
    from requests_core.http_manager.contrib.securetransport import (inject_into_urllib3,
                                                 extract_from_urllib3)
except ImportError as e:
    pytestmark = pytest.mark.skip('Could not import SecureTransport: %r' % e)

pytestmark = pytest.mark.skip('SecureTransport currently not supported on v2!')

from ..with_dummyserver.test_https import TestHTTPS, TestHTTPS_TLSv1  # noqa: F401
from ..with_dummyserver.test_socketlevel import (  # noqa: F401
    TestSNI, TestSocketClosing, TestClientCerts
)


def setup_module():
    inject_into_urllib3()


def teardown_module():
    extract_from_urllib3()
