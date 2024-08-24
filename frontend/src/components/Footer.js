import { Box, Container, Link, Stack, Typography } from "@mui/material";
import { Component } from "react";


class Footer extends Component {
    render () {
        return (
            // <Container
            // className="bg-[#8dc2cb] mx- sm:mx-auto max-w-7xl"
            // component="div"
            // fixed="false"
            // maxWidth="xl"

            // >
            //     <Box
            //     sx={{
            //     display: 'flex',
            //     flexDirection: 'column',
            //     justifyContent:'space-between'
            //     }}
            //     >
            //         <Stack
            //         spacing="48px"
            //         >
            //             <Link
            //             >
            //                 <Typography
            //                 variant="h6"
            //                 >Отзывы
            //                 </Typography>
            //             </Link>
            //             <Link
            //             >
            //                 <Typography
            //                 variant="h6"
            //                 >
            //                     Контактная информация
            //                 </Typography>
            //             </Link>
            //         </Stack>
            //     </Box>
            // </Container>

            <div className="md:mx-auto md:container bg-slate-400 rounded-md justify-center sm:mx-12">
                <div className="flex justify-between">
                    <div className="flex flex-col gap-y-8 md:px-3">
                        <a href="#" className="px-1 text-lg font-sans">Контактная информация</a>
                        <a href="#" className="px-1 text-lg font-sans">Отзывы</a>
                    </div>
                </div>
            </div>
        )
    }
};

export default Footer;
