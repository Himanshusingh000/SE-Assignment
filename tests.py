import unittest as UT
import pytest
import otpassign as OTP
class TestOtp(UT.TestCase):
    def test_validatemail(self):
        result = OTP.validatEmailID("himanshujamwal000@gmai.com")
        expected = True
        self.assertEqual(result, expected)

    def test_validatemail(self):
        result = OTP.validatEmailID("himanshujamwalgmaicom")
        expected = True
        self.assertEqual(result, expected)

    def test_generateotp(self):
        otp_len = len(OTP.generateOtp())
        expected_len = 6
        self.assertEqual(otp_len, expected_len)
        resut_type = OTP.generateOtp()
        otp_type = resut_type.isdigit()
        expected_type = True
        self.assertEqual(otp_type, expected_type)
if __name__ == '__main__':
    pytest.main()