import React, { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";
import makeRequest from "../utils/functions";
import { ROOT_API } from "..";

const PasswordResetForm = () => {
  const { uidb64, token } = useParams();
  const [isValidToken, setIsValidToken] = useState(false);
  const [errorMessage, setErrorMessage] = useState('');
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");

  const navigate = useNavigate();

  useEffect(() => {
    const checkToken = async () => {
      try {
        let response = await makeRequest(
          `${ROOT_API}users/api/v1/reset-password-confirm/${uidb64}/${token}`,
          "GET",
        );

        if (response.status === 200) {
          setIsValidToken(true);
        }

        else {
          setIsValidToken(false);
          setErrorMessage("Invalid or expired token. Please request a new reset link.");
        }

      } catch (error) {
        setIsValidToken(false);
        console.log("Token is invalid or expired.");
      }
    };
    checkToken();
  }, [uidb64, token]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
        let response = await makeRequest(
            `${ROOT_API}users/api/v1/update-password/${uidb64}/`,
            "POST",
            {
                "password1": password,
                "password2": confirmPassword,
            },
        )

        if (response.status === 200) {
          console.log("Password has been reset successfully")
          navigate("/reset-password-success", { replace: true })
        }

    } catch (error) {
        setErrorMessage('Error resetting password.');
        console.log("Error:", error)
    }
  };

  return (
    <div class="flex flex-col justify-center items-center bg-zinc-950 h-max min-h-[100vh] pb-5">
      <div class="mx-auto flex w-full flex-col justify-center px-5 pt-0 md:h-[unset] md:max-w-[50%] lg:h-[100vh] min-h-[100vh] lg:max-w-[50%] lg:px-6">
        <div class="my-auto mb-auto mt-8 flex flex-col md:mt-[70px] w-[350px] max-w-[450px] mx-auto md:max-w-[450px] lg:mt-[130px] lg:max-w-[450px]">
          <p class="text-[32px] font-bold text-white">Create new password</p>
          <p class="mb-2.5 mt-2.5 font-normal text-zinc-400">
            Please, insert new passwords
          </p>
          <div class="relative my-4">
            <div class="relative flex items-center py-1">
              <div class="grow border-t border-zinc-800"></div>
              <div class="grow border-t border-zinc-800"></div>
            </div>
          </div>
          <div>
            {isValidToken ? (
                <form onSubmit={handleSubmit} class="mb-4">
                <div class="grid gap-2">
                    <div class="grid gap-1">
                    <label class="text-white" for="password">
                        Password
                    </label>
                    <input
                        id="password1"
                        placeholder="Password"
                        type="password"
                        value={password}
                        autocomplete="current-password"
                        class="mr-2.5 mb-2 h-full min-h-[44px] w-full rounded-lg border bg-zinc-950 text-white border-zinc-800 px-4 py-3 text-sm font-medium placeholder:text-zinc-400 focus:outline-0 dark:border-zinc-800 dark:bg-transparent dark:text-white dark:placeholder:text-zinc-400"
                        onChange={(e) => setPassword(e.target.value)}
                    />
                    <label class="text-white" for="password">
                        Confirm Password
                    </label>
                    <input
                        id="password2"
                        placeholder="Password"
                        type="password"
                        value={confirmPassword}
                        autocomplete="current-password"
                        class="mr-2.5 mb-2 h-full min-h-[44px] w-full rounded-lg border bg-zinc-950 text-white border-zinc-800 px-4 py-3 text-sm font-medium placeholder:text-zinc-400 focus:outline-0 dark:border-zinc-800 dark:bg-transparent dark:text-white dark:placeholder:text-zinc-400"
                        onChange={(e) => setConfirmPassword(e.target.value)}
                    />
                    </div>
                    {errorMessage && <p style={{ color: "red" }}>{errorMessage}</p>}
                    <button
                    type="submit"
                    class="whitespace-nowrap ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 bg-white text-zinc-950 hover:bg-white/90 active:bg-white/80 flex w-full max-w-full mt-6 items-center justify-center rounded-lg px-4 py-4 text-base font-medium"
                    >
                    Reset Password
                    </button>
                </div>
                </form>
            ) : (
                <p>Invalid or expired token. Please request a new reset link.</p>
            )};
          </div>
        </div>
      </div>
    </div>
  );
};

export default PasswordResetForm;
