import React, { Component, useState } from "react";

import AppBar from '@mui/material/AppBar'
import MenuIcon from '@mui/icons-material/Menu';
import Typography from "@mui/material/Typography";
import { IconButton, Toolbar } from "@mui/material";
import {Link} from 'react-router-dom'
import { GiShoppingCart } from "react-icons/gi";


// function ThemeSwitcher() {
//   const prefersDarkMode = useMediaQuery('(prefers-color-scheme: dark)');

//   const theme = React.useMemo(
//     () =>
//       createTheme({
//         palette: {
//           mode: prefersDarkMode ? 'dark' : 'light',
//         },
//       }),
//     [prefersDarkMode],
//   );

//   return (
//     <ThemeProvider theme={theme}>
//       <CssBaseline />
//     </ThemeProvider>
//   );
// }


// function MenuPopup() {
//   const [opened, setOpened] = useState(0);

//   function openPopup() {
//     setOpened(1);
//   }
// };


export default function Header() {
  return (
    <AppBar>
    <Toolbar sx={{display: "flex"}}>
      <IconButton
        size="large"
        edge="start"
        color="inherit"
        aria-label="open drawer"
        sx={{ mr: 2 }}
        >
          <MenuIcon />
      </IconButton>
      <Typography
        variant="h6"
        noWrap
        component="div"
        sx={{ display: { xs: 'none', sm: 'block' } }}
        >
        Anifigure Shop
      </Typography>
      <Link to="/login" />
      <GiShoppingCart />
    </Toolbar>
  </AppBar>
  )
}


// class Header extends Component {
//     render() {
//         return (
          // <header className="bg-while">
          //   <nav className="mx-auto flex max-w items-center justify-between p-6 lg:px-12" aria-label="Global">

          //     <div className="flex lg:flex-1">
          //       <a href="#">
          //         <img className="h-8 w-auto" src="#"></img>
          //       </a>
          //     </div>

          //     <div>

          //     </div>

          //   </nav>
          // </header>
  
//           <AppBar>
//             <Toolbar>
//               <IconButton
//                 size="large"
//                 edge="start"
//                 color="inherit"
//                 aria-label="open drawer"
//                 sx={{ mr: 2 }}
//                 >
//                   <MenuIcon />
//               </IconButton>
//               <Typography
//                 variant="h6"
//                 noWrap
//                 component="div"
//                 sx={{ display: { xs: 'none', sm: 'block' } }}
//                 >
//                 Anifigure Shop
//               </Typography>
//             </Toolbar>
//           </AppBar>  
//         )
//     }
// };

// export default Header;
