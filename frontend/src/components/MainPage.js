import axios from 'axios'
import { Box, Container, Divider, Stack, Typography, Card, CardContent } from "@mui/material";
import CardMedia from '@mui/material/CardMedia';
import CardActions from '@mui/material/CardActions';
import Button from '@mui/material/Button';
import Grid from '@mui/material/Grid';
import { Component, useEffect, useState } from "react";
import { ROOT_API } from '../index'


const makeRequest = async (url, method = "POST", data = {}, headers = {}) => {
  const response = await axios({
      url,
      method,
      data,
      headers: headers,
      timeout: 20000
    });
  return response.data
};


const ProductsComponent = () => {
    const [products, setProducts] = useState([]);

    const [quantity, setQuantity] = useState(0);


    const handlePurchase = async (product, updatedQuantity, updateQuantity = false) => {
      setQuantity(updatedQuantity)

      try {
        const access_token = localStorage.getItem("access")
        console.log(access_token)
        const response = await makeRequest(`${ROOT_API}/api/carts/purchase/`, "POST", {
          product: product,
          quantity: updatedQuantity,
          updateQuantity: updateQuantity
        }, {
          Authorization: `Bearer ${access_token}`
        })
        console.log('Purchase response:', response);

      } catch (error) {
        console.log('Error while sending post request to /api/purchase/', error);
      }
    }

    const handleBuyClick = async (product) => {
      const updatedQuantity = 1
      handlePurchase(product, updatedQuantity)
    };
  
    const handleIncrement = async (product) => {
      const updatedQuantity = quantity + 1
      handlePurchase(product, updatedQuantity, true)
    };

    const handleDecrement = async (product) => {
      const updatedQuantity = quantity > 1 ? quantity - 1 : 0
      handlePurchase(product, updatedQuantity, true)
    };

    useEffect(() => {
        const fetchProducts = async () => {
            console.log("Fetching products...");
            try {
                const response = await axios.get(`${ROOT_API}/api/products/`);
                console.log("Response data:", response.data);
                setProducts(response.data.results);
            } catch (error) {
                console.error("Error fetching products:", error);
            }
        };

        fetchProducts();
    }, []); // Пустой массив зависимостей означает, что эффект выполнится только один раз при монтировании компонента

    return (
        <>
          <div className='mx-auto container'>
            <aside className='mx-auto'>
              <div>

              </div>
            </aside>
            <div className='grid sm:grid-cols-3 md:grid-cols-4 gap-5 grid-cols-1 gap-y-12'>
              {Array.isArray(products) && products.map((product) => (
                
                <div key={product.pk} className='flex-col'>
                  <div className='flex-col space-y-2 border border-solid shadow-md'>
                    <div className='flex items-center justify-center'>
                      <div className='w-full h-64 overflow-hidden'>
                        <img
                        className='object-contain w-full h-full'
                        src={product.images && product.images.length > 0 ? product.images[0].image : 'default_image_url'}>
                        </img>
                      </div>
                    </div>
                    <div className='block-inline mx-1 sm:mx-2'>
                      <h4 className='font-sans text-xl'>{product.name}</h4>
                    </div>
                    <div className='block-inline mx-1 sm:mx-2'>
                      <span className='font-sans'>{product.description}</span>
                    </div>
                    <div className='flex justify-around'>
                      <div>
                        <span className='font-sans'>{product.price} Рублей</span>
                      </div>
                      <div>
                        { quantity == 0 ? (
                          <button className='bg-indigo-500 hover:bg-indigo-800 p-3 rounded-md' quantity={quantity} onClick={() => handleBuyClick(product)}>
                            <span className='text-white font-sans'>Купить</span>
                          </button>
                        ) : (
                          <div className='flex items-center space-x-2'>
                            <button className='bg-gray-300 hover:bg-gray-400 p-2 rounded-md' quantity={quantity} onClick={() => handleDecrement(product)}>
                              <span className='text-black font-sans'>-1</span>
                            </button>
                            <span className='font-sans'>{quantity}</span>
                            <button className='bg-gray-300 hover:bg-gray-400 p-2 rounded-md' quantity={quantity} onClick={() => handleIncrement(product)}>
                              <span className='text-black font-sans'>+1</span>
                            </button>
                          </div>
                        )}
                      </div>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
          {/* <Grid container spacing={{ xs: 2, md: 3 }} columns={{ xs: 4, sm: 8, md: 12 }}>
            {Array.isArray(products) && products.map((product) => (
              <Grid item xs={2} sm={3} md={4}>
                <Card
                key={product.pk}
                sx={{ margin: 2, maxWidth: 305 }}
                >
                  <CardContent
                  sx={{ marginY: 2 }}
                  >
                    <CardMedia
                    component="img"
                    height={"1"}
                    image={product.images && product.images.length > 0 ? product.images[0].image : 'default_image_url'}
                    alt={product.name}
                    >
                    </CardMedia>
                    <Typography
                      component="div"
                      variant='h5'
                      >
                          {product.name}
                      </Typography>
                      <Typography
                      variant='h6'
                      >
                          {product.description}
                      </Typography>
                      <Typography
                      >
                          {product.price} Рублей
                      </Typography>
                      <CardActions>
                        <Button variant='outlined' size='medium'>Купить</Button>
                      </CardActions>
                  </CardContent>
                </Card>
              </Grid>
            ))}
          </Grid> */}

          {/* {Array.isArray(products) && products.map((product) => (
              <Card
              key={product.pk}
              sx={{ margin: 2, maxWidth: 305 }}
              >
                  <CardContent
                  sx={{ marginY: 2 }}
                  >
                      <CardMedia
                          component="img"
                          height="50"
                          image={product.images && product.images.length > 0 ? product.images[0].image : 'default_image_url'}

                          alt={product.name}
                      >
                      </CardMedia>
                      <Typography
                      component="div"
                      variant='h5'
                      >
                          {product.name}
                      </Typography>
                      <Typography
                      variant='h6'
                      >
                          {product.description}
                      </Typography>
                      <Typography
                      >
                          {product.price} Рублей
                      </Typography>
                  </CardContent>
              </Card>
          ))} */}
        </>



        // <div>
        //     {Array.isArray(products) && products.map((product) => (
        //         <div key={product.id}>
        //             <h3>{product.name}</h3>
        //             <p>{product.description}</p>
        //         </div>
        //     ))}
        // </div>
    );
};



class MainPage extends Component {
    render () {
        return (
            <Container
            sx={{"pt": "160px", "mt": "120px"}}
            maxWidth="xl"
            >
                <Stack
                spacing={4}
                divider={<Divider orientation="horizontal"/>}
                >
                    <Typography
                    variant="h3"
                    component="h2"
                    fontFamily="sans-serif"
                    color="navy"
                    >
                        Anifigure Shop
                    </Typography>
                    <div className='bg-slate-300 object-fill'>
                      <Typography
                      className='font-sans text-violet-700'
                      >
                        Добро пожаловать в наш интернет-магазин, где оживают ваши любимые аниме и манга персонажи! 
                        Мы предлагаем широкий ассортимент аниме фигурок, которые порадуют как настоящих коллекционеров, 
                        так и тех, кто только начинает погружаться в удивительный мир японской поп-культуры. 
                        Каждая фигурка в нашем каталоге тщательно отобрана и представляет собой уникальное произведение искусства. 
                        От культовых героев классических аниме до новинок из самых популярных сериалов — у нас вы найдете персонажей, 
                        которые вдохновляют, восхищают и дарят радость. Но это еще не всё! В скором времени наш ассортимент 
                        будет пополняться новыми категориями товаров, чтобы предложить вам ещё больше аниме-радости. 
                        В нашем магазине вы сможете найти не только фигурки, но и многое другое: аксессуары, постеры, 
                        одежду и предметы коллекционирования, которые подчеркнут вашу любовь к аниме и станут отличным подарком 
                        для друзей и близких. Мы стремимся сделать ваш опыт покупок не только удобным, но и незабываемым. 
                        Наслаждайтесь качеством, эксклюзивностью и удивительным разнообразием нашего ассортимента. 
                        Добро пожаловать в мир, где каждая деталь напоминает вам о ваших любимых аниме и манга историях!
                      </Typography>
                    </div>
                </Stack>
                <Box
                    display="flex"
                    flexDirection="row"
                    sx={{ marginY: 2, marginX: 4 }}
                    >
                        <ProductsComponent />
                </Box>
            </Container>
        )
    }
};

export default MainPage;
