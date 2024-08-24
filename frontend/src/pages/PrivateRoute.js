import { Route, Routes } from "react-router-dom"


const PrivateRoute = ({ Component, ...rest }) => {

	console.log("Private Router works!")
	return (
		Component
	)
}

export default PrivateRoute;
