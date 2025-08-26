import { Component, useEffect, useState, useContext } from "react";

const CartPageComponent = () => {
	return (
		<div>
			<h1>Cart</h1>
		</div>
	)
}

class CartComponent extends Component {
  render() {
    return (
      <div>
        <CartPageComponent></CartPageComponent>
      </div>
    );
  }
}

export default CartComponent;
