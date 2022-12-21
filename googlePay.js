const paymentRequest = payments.paymentRequest({
  countryCode: 'US',
  currencyCode: 'USD',
  total: {
    amount: '5.79',
    label: 'Total'
  },
});

const googlePay = await payments.googlePay(paymentRequest);
await googlePay.attach('#googlePay');

const googlePayButtonTarget = document.getElementById('googlePay');
googlePayButtonTarget.onclick = async () => {
  const tokenResult = await googlePay.tokenize();

  // Pass `tokenResult.token` to your server, and then call the /v2/payments API
  // to complete the payment
}
