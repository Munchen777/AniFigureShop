import { Component } from "react";


class Footer extends Component {
    render () {
        return (
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
