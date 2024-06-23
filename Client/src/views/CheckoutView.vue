<template>
  <div class="untree_co-section">
    <div class="container">
      <div class="row">
        <div class="col-md-6 mb-5 mb-md-0">
          <h2 class="h3 mb-3 text-black">اطلاعات سفارش</h2>
          <div class="p-3 p-lg-5 border bg-white">
            <div class="form-group row">
              <div class="col-md-6">
                <label for="c_fname" class="text-black">نام <span class="text-danger">*</span></label>
                <input type="text" class="form-control" id="c_fname" name="c_fname">
              </div>
              <div class="col-md-6">
                <label for="c_lname" class="text-black">نام خانوادگی <span class="text-danger">*</span></label>
                <input type="text" class="form-control" id="c_lname" name="c_lname">
              </div>
            </div>


            <div class="form-group row">
              <div class="col-md-12">
                <label for="c_address" class="text-black">آدرس <span class="text-danger">*</span></label>
                <input type="text" class="form-control" id="c_address" name="c_address" placeholder="Street address">
              </div>
            </div>


            <div class="form-group row">
              <div class="col-md-6">
                <label for="c_state_country" class="text-black">شماره تماس </label>
                <input type="text" class="form-control" id="c_state_country" name="c_state_country">
              </div>
              <div class="col-md-6">
                <label for="c_postal_zip" class="text-black">ایمیل </label>
                <input type="text" class="form-control" id="c_postal_zip" name="c_postal_zip">
              </div>
            </div>

            <div class="form-group">
              <label for="c_order_notes" class="text-black">توضیحات</label>
              <textarea name="c_order_notes" id="c_order_notes" cols="30" rows="5" class="form-control"
                        placeholder="توضیحات خود را بنویسید..."></textarea>
            </div>
          </div>
        </div>
        <div class="col-md-6">


          <div class="row mb-5">
            <div class="col-md-12">
              <h2 class="h3 mb-3 text-black">Your Order</h2>
              <div class="p-3 p-lg-5 border bg-white">
                <table class="table site-block-order-table mb-5">
                  <thead>
                  <th>Product</th>
                  <th>Total</th>
                  </thead>
                  <tbody>
                  <tr>
                    <td>لپ تاپ  1<strong class="mx-2">x</strong></td>
                    <td>250.00</td>
                  </tr>
                  <tr>
                    <td>گوشی موبایل  1<strong class="mx-2">x</strong></td>
                    <td>100.00</td>
                  </tr>
                  <tr>
                    <td class="text-black font-weight-bold"><strong>جمع کل</strong></td>
                    <td class="text-black font-weight-bold"><strong>350.00</strong></td>
                  </tr>
                  </tbody>
                </table>

                <div class="border p-3 mb-3">
                  <h3 class="h6 mb-0"><a class="d-block" data-bs-toggle="collapse" href="#collapsebank" role="button"
                                         aria-expanded="false" aria-controls="collapsebank">Direct Bank Transfer</a>
                  </h3>

                  <div class="collapse" id="collapsebank">
                    <div class="py-2">
                      <p class="mb-0">Make your payment directly into our bank account. Please use your Order ID as the
                        payment reference. Your order won’t be shipped until the funds have cleared in our account.</p>
                    </div>
                  </div>
                </div>

                <div class="border p-3 mb-3">
                  <h3 class="h6 mb-0"><a class="d-block" data-bs-toggle="collapse" href="#collapsecheque" role="button"
                                         aria-expanded="false" aria-controls="collapsecheque">Cheque Payment</a></h3>

                  <div class="collapse" id="collapsecheque">
                    <div class="py-2">
                      <p class="mb-0">Make your payment directly into our bank account. Please use your Order ID as the
                        payment reference. Your order won’t be shipped until the funds have cleared in our account.</p>
                    </div>
                  </div>
                </div>

                <div class="border p-3 mb-5">
                  <h3 class="h6 mb-0"><a class="d-block" data-bs-toggle="collapse" href="#collapsepaypal" role="button"
                                         aria-expanded="false" aria-controls="collapsepaypal">Paypal</a></h3>

                  <div class="collapse" id="collapsepaypal">
                    <div class="py-2">
                      <p class="mb-0">Make your payment directly into our bank account. Please use your Order ID as the
                        payment reference. Your order won’t be shipped until the funds have cleared in our account.</p>
                    </div>
                  </div>
                </div>

                <div class="form-group">
                  <button class="btn btn-black btn-lg py-3 btn-block" onclick="window.location='thankyou.html'">Place
                    Order
                  </button>
                </div>

              </div>
            </div>
          </div>

        </div>
      </div>
      <!-- </form> -->
    </div>
  </div>
</template>

<script>
export default {
  name: "CheckoutView"
}
</script>

