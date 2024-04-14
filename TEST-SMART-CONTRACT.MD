COMMAND
```
Truffle test --show-events
```

<b><i>1. test/TestRideShare.js </i></b> <br>
* Test 1: AddPassenger, thêm hành khách vào hệ thống <br>
* Test 2: CreateRide, tạo 1 chuyến đi <br>
* Test 3: CreateRide and JoinRide, tạo 1 chuyến đi và 1 passenger join vào chuyến đi đó, 2 tài khoản khác nhau <br>
* Test 4: CreateRide and JoinRide, tạo 1 chuyến đi và 1 passenger join vào chuyến đi đó, 2 tài khoản giống nhau <br>
* Test 5: CreateRide and JoinRide, tạo 1 chuyến đi và 2 passenger join vào chuyến đi đó, 3 tài khoản khác nhau <br>
* Test 6: AddPassenger, CreateRide, JoinRide and ConfirmDriverMet, tạo 1 request từ 1 hành khách để yêu cầu tạo 1 chuyến đi bởi tài xế, hành khách thực hiện tham gia vào chuyến đi đó, tài xê confirm khi gặp được passenger. <br>
* Test 7: AddPassenger, CreateRide, JoinRide, ConfirmDriverMet and Arrived tạo 1 request từ 1 hành khách để yêu cầu tạo 1 chuyến đi bởi tài xế, hành khách thực hiện tham gia vào chuyến đi đó, tài xế confirm khi gặp được passenger, tài xế rút tiền từ transaction khi đã thực hiện xong chuyến đi. <br>
* Test 8: AddPassenger, CreateRide, JoinRide, ConfirmDriverMet and Cancel From Driver, tạo 1 request từ 1 hành khách để yêu cầu tạo 1 chuyến đi bởi tài xế, hành khách thực hiện tham gia vào chuyến đi đó, tài xế confirm khi gặp được passenger, tài xế hủy chuyến đi đó, chi phí chuyến đi được chia đều và bồi thường cho các hành khách <br>
* Test 9: AddPassenger, CreateRide, JoinRide, ConfirmDriverMet and Cancel From Passenger, tạo 1 request từ 1 hành khách để yêu cầu tạo 1 chuyến đi bởi tài xế, hành khách thực hiện tham gia vào chuyến đi đó, tài xế confirm khi gặp được passenger, 1 hành khách hủy chuyến đi đó, chi phí chuyến đi trong smart contract được chuyển vào tài khoản của tài xế <br>
* Test 10: AddPassenger, CreateRide, JoinRide, ConfirmDriverMet and Cancel From Passenger, tạo 1 request từ 1 hành khách để yêu cầu tạo 1 chuyến đi bởi tài xế, hành khách thực hiện tham gia vào chuyến đi đó, tài xế confirm khi gặp được passenger, smart contract có 2 hành khách, 1 hành khách hủy chuyến đi đó, 1 hành khách vẫn đi, tiền trong smart contract chuyển cho tài xế trong lần có hành khách hủy chuyến sau đó, khi thực hiện chuyến đi xong tiền trong smart contract tiếp tục chuyển cho tài xế <br>