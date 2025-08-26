import { useState, useContext } from "react";
import { useNavigate, Link } from "react-router-dom";
import AuthContext from "../contexts/AuthContext";

const ResetPassword = () => {
  const { resetPassword } = useContext(AuthContext);

  const [email, setEmail] = useState("");

  return (
    <div class="flex flex-col justify-center items-center bg-zinc-950 h-max min-h-[100vh] pb-5">
      <div class="mx-auto flex w-full flex-col justify-center px-5 pt-0 md:h-[unset] md:max-w-[50%] lg:h-[100vh] min-h-[100vh] lg:max-w-[50%] lg:px-6">
        <div class="my-auto mb-auto mt-8 flex flex-col md:mt-[70px] w-[350px] max-w-[450px] mx-auto md:max-w-[450px] lg:mt-[130px] lg:max-w-[450px]">
          <p class="text-[32px] font-bold text-white">Reset Password</p>
          <p class="mb-2.5 mt-2.5 font-normal text-zinc-400">
            Enter your email to receive a link to reset your password
          </p>
          <div class="relative my-4">
            <div class="relative flex items-center py-1">
              <div class="grow border-t border-zinc-800"></div>
              <div class="grow border-t border-zinc-800"></div>
            </div>
          </div>
          <div>
            <form onSubmit={(e) => resetPassword(e)} class="mb-4">
              <div class="grid gap-2">
                <div class="grid gap-1">
                  <label class="text-white" for="email">
                    Email
                  </label>
                  <input
                    class="mr-2.5 mb-2 h-full min-h-[44px] w-full rounded-lg border bg-zinc-950 text-white border-zinc-800 px-4 py-3 text-sm font-medium placeholder:text-zinc-400 focus:outline-0 dark:border-zinc-800 dark:bg-transparent dark:text-white dark:placeholder:text-zinc-400"
                    id="email"
                    placeholder="name@example.com"
                    type="email"
                    autocapitalize="none"
                    autocomplete="email"
                    autocorrect="off"
                    name="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                  />
                </div>
                <button
									type="submit"
                  class="whitespace-nowrap ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 bg-white text-zinc-950 hover:bg-white/90 active:bg-white/80 flex w-full max-w-full mt-6 items-center justify-center rounded-lg px-4 py-4 text-base font-medium"
                >
                  Send reset link
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ResetPassword;
