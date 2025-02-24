import React, { Component, useContext, useState } from "react";

import { Link } from "react-router-dom";
import AuthContext from "../contexts/AuthContext";
import { PiShoppingCartDuotone } from "react-icons/pi";
import { VscAccount } from "react-icons/vsc";

export default function Header() {
  let { user, loginUser, logoutUser } = useContext(AuthContext);

  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);
  const [isDropdownOpen, setisDropdownOpen] = useState(false);
  const [cartItemsCount, setCartItemsCount] = useState(0);

  return (
    <header className="bg-white">
      <nav className="mx-auto flex max-w-7xl items-center justify-between p-6 lg:px-8">
        <div className="flex lg:flex-1">
          <a href="#">Логотип</a>
        </div>

        {/* Кнопка для открытия меню на мобильных устройствах */}
        <div className="flex lg:hidden">
          <button
            type="button"
            onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
            className="-m-2.5 inline-flex items-center justify-center rounded-md p-2.5 text-gray-700"
          >
            <svg
              className="h-6 w-6"
              fill="none"
              viewBox="0 0 24 24"
              strokeWidth="1.5"
              stroke="currentColor"
              aria-hidden="true"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5"
              />
            </svg>
          </button>
        </div>

        {/* Меню для крупных экранов */}
        <div className="hidden lg:flex lg:gap-x-12 items-center">
          <a href="#" className="text-sm font-semibold text-gray-900">
            Каталог
          </a>
          {/* <a href="#" className="text-sm font-semibold text-gray-900">Marketplace</a> */}
          <a href="#" className="text-sm font-semibold text-gray-900">
            О компании
          </a>
        </div>

        <div className="hidden lg:flex lg:flex-1  relative lg:justify-evenly items-center">
          <div className="flex relative">
            <Link to={"/cart"}>
              <PiShoppingCartDuotone className="w-5 h-5" />
              {cartItemsCount > 0 && (
                <span className="absolute -bottom-1 -right-1 bg-red-500 text-white text-xs rounded-full h-4 w-4 flex items-center justify-center">
                  {cartItemsCount}
                </span>
              )}
            </Link>
          </div>
          {/* <div className="flex">
            <Link
              to={"/cart"}
            >
              <PiShoppingCartDuotone className="w-5 h-5" />
            </Link>
          </div> */}
          {user ? (
            <div className="relative group">
              <button
                className="flex items-center p-2 rounded-full hover:bg-gray-100 transition-colors"
                onMouseEnter={() => setisDropdownOpen(true)}
                onMouseLeave={() => setisDropdownOpen(false)}
              >
                <VscAccount className="w-6 h-6"/>
              </button>

              {/* Выпадающий блок */}
              {isDropdownOpen && (
                <div
                  className="absolute right-0 w-48 bg-white text-black shadow-md rounded-md z-10 dark:bg-zinc-50"
                  onMouseEnter={() => setisDropdownOpen(true)}
                  onMouseLeave={() => setisDropdownOpen(false)}
                >
                  <Link
                    to={"/profile"}
                    className="block w-full text-left px-4 py-2 hover:bg-gray-100"
                  >
                    Профиль
                  </Link>
                  <Link
                    onClick={logoutUser}
                    className="block w-full text-left px-4 py-2 hover:bg-gray-100"
                  >
                    Выйти
                  </Link>
                </div>
              )}
            </div>
          ) : (
            <div className="flex items-center space-x-4">
              <Link
                to="/login"
                className="text-sm font-semibold text-gray-900 hover:text-gray-700 transition-colors"
              >
                Login
              </Link>
              <span className="h-4 w-px bg-gray-300"></span>
              <Link
                to="/register"
                className="text-sm font-semibold text-gray-900 hover:text-gray-700 transition-colors"
              >
                Register
              </Link>
            </div>
            // <Link
            // to="/login"
            // className="text-sm font-semibold text-gray-900"
            // >
            //   Login
            // </Link>
          )}
        </div>
      </nav>

      {/* Мобильное меню */}
      {isMobileMenuOpen && (
        <div className="lg:hidden">
          <div className="space-y-2 p-4">
            <a href="#" className="block text-sm font-semibold text-gray-900">
              Каталог
            </a>
            {/* <a href="#" className="block text-sm font-semibold text-gray-900">Marketplace</a> */}
            <a href="#" className="block text-sm font-semibold text-gray-900">
              О компании
            </a>
            <hr className="my-2" />
            {user ? (
              <Link
                className="flex items-center w-full text-sm font-semibold text-gray-900 hover:bg-gray-100 rounded-md p-2"
                onClick={() => setisDropdownOpen(!isDropdownOpen)}
                // onMouseEnter={() => setisDropdownOpen(true)}
                // onMouseLeave={() => setisDropdownOpen(false)}
              >
                {user.username || user.email}
              </Link>
            ) : (
              <div className="flex flex-col space-y-2">
                <Link
                  to="/login"
                  className="block w-full text-sm font-semibold text-gray-900 hover:bg-gray-100 rounded-md transition-colors"
                >
                  Login
                </Link>
                <Link
                  to="/register"
                  className="block w-full text-sm font-semibold text-gray-900 hover:bg-gray-100 rounded-md transition-colors"
                >
                  Register
                </Link>
              </div>
            )}

            {isDropdownOpen && (
              <div
                onMouseEnter={() => setisDropdownOpen(true)}
                onMouseLeave={() => setisDropdownOpen(false)}
                className="relative"
              >
                <button className="block w-full text-left px-4 py-2 hover:bg-gray-100">
                  Профиль
                </button>
                <button
                  className="block w-full text-left px-4 py-2 hover:bg-gray-100"
                  onClick={logoutUser}
                >
                  Выйти
                </button>
              </div>
            )}
          </div>
        </div>
      )}
    </header>
  );
}
