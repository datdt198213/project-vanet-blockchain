import Web3 from 'web3';
import RideShare from "../contracts/RideShare.json";

const web3 = new Web3(window.ethereum);
const contractABI = RideShare.abi;
const networkID = await web3.eth.net.getId();
const deployedNetwork = await RideShare.networks[networkID];
const accounts = await web3.eth.getAccounts();
const contract = new web3.eth.Contract(contractABI, deployedNetwork && deployedNetwork.address);

export const getCreateRides = async (account) => {
    
    try {
        const createRides = await contract.methods.getCreateRides(account).call();
        
        return createRides;
    } catch (error) {
        console.error('Error fetching created rides: ', error);
        return [];
    }
}

// Hàm lấy chi tiết của một chuyến đi từ hợp đồng thông minh
export const getRideDetails = async (rideId) => {
    try {
      // Gọi hàm rides trên hợp đồng thông minh để lấy thông tin chi tiết của chuyến đi
      //console.log('ID from getRideDetails: ' + rideId);
      const rideDetails = await contract.methods.rides(rideId).call();
     // console.log('Ride Detail: ' + rideDetails);
      // Trả về thông tin chi tiết của chuyến đi
      return rideDetails;
    } catch (error) {
      // Xử lý lỗi nếu có
      throw new Error('Error fetching ride details: ' + error.message);
    }
  };