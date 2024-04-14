COMMAND
```
Truffle test --show-events
```

Test 1: AddPassenger, thêm hành khách vào hệ thống <br>
Test 2: CreateRide, tạo 1 chuyến đi <br>
Test 3: CreateRide and JoinRide, tạo 1 chuyến đi và 1 passenger join vào chuyến đi đó, 2 tài khoản khác nhau <br>
Test 4: CreateRide and JoinRide, tạo 1 chuyến đi và 1 passenger join vào chuyến đi đó, 2 tài khoản giống nhau <br>
Test 5: CreateRide and JoinRide, tạo 1 chuyến đi và 2 passenger join vào chuyến đi đó, 3 tài khoản khác nhau <br>
Test 6: AddPassenger, CreateRide, JoinRide and ConfirmDriverMet, tạo 1 request từ 1 hành khách để yêu cầu tạo 1 chuyến đi bởi tài xế, hành khách thực hiện tham gia vào chuyến đi đó, tài xê confirm khi gặp được passenger. <br>
Test 7: AddPassenger, CreateRide, JoinRide, ConfirmDriverMet and Arrived tạo 1 request từ 1 hành khách để yêu cầu tạo 1 chuyến đi bởi tài xế, hành khách thực hiện tham gia vào chuyến đi đó, tài xế confirm khi gặp được passenger, tài xế rút tiền từ transaction khi đã thực hiện xong chuyến đi. <br>