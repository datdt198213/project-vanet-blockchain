import React, { useState, useEffect } from 'react';
import { getRideDetails , getCreateRides} from './api';
import { Card, Table } from 'react-bootstrap';

const RideInfor = ({account}) => {
    const [rideDetails, setRideDetails] = useState([]);

    useEffect(() => {
      // const fetchRideCreate = async (address) => {

      //   const history = await getRideDetails(rideId);
      const fetchRideCreate = async () => {
        try {
          // }
          const createRides = await getCreateRides(account);
          setRideDetails(createRides);
          const rides = await Promise.all(createRides.map(async (rideId) => {
            const rd = await getRideDetails(rideId);
            return {
              id: rideId,
              drivingCost: parseInt(rd[2]),
              capacity: parseInt(rd[3]),
              confirmedAt: new Date(Number(rd[4]) * 1000).toLocaleString(),
              originAddress: rd[5],
              destAddress: rd[6],
              numOfPassengers: parseInt(rd[7])
            }
          }))
          setRideDetails(rides);
        } catch (error) {
          console.error('Error fetching ride creates');
        }
      }
      fetchRideCreate()
    }, [account]);

    if(rideDetails.length === 0) {
      <h2 style={{marginTop: '20px', marginBottom: '20px'}}>Ride Detail</h2>
      return <p>No ride history found</p>
    }
    return (<div>
      <h2 style={{marginTop: '20px', marginBottom: '20px'}}>Ride Detail</h2>
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>Nơi bắt đầu - Nơi kết thúc</th>
            <th>Thời gian bắt đầu</th>
            <th>Chi Phí (ETH)</th>
            <th>Số người tối đa</th>
            <th>Số người hiện tại</th>
          </tr>
        </thead>
        <tbody>
          {rideDetails.map((ride, index) => (
            <tr key={index}>
              <td>{ride.originAddress} - {ride.destAddress}</td>
              <td>{ride.confirmedAt}</td>
              <td>{ride.drivingCost}</td>
              <td>{ride.capacity}</td>
              <td>{ride.numOfPassengers}</td>
            </tr>
          ))}
        </tbody>
      </Table>

    </div>)
  }

export default RideInfor;