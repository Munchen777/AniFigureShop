import { useNavigate } from 'react-router-dom';

const ResetPasswordDone = () => {
  const navigate = useNavigate();

  return (
    <div class="flex flex-col justify-center items-center bg-zinc-950 h-max min-h-[100vh] pb-5">
      <div class="mx-auto flex w-full flex-col justify-center px-5 pt-0 md:h-[unset] md:max-w-[50%] lg:h-[100vh] min-h-[100vh] lg:max-w-[50%] lg:px-6">
        <div class="my-auto mb-auto mt-8 flex flex-col md:mt-[70px] w-[350px] max-w-[450px] mx-auto md:max-w-[450px] lg:mt-[130px] lg:max-w-[450px]">
          <p class="text-[32px] font-bold text-white">Reset Password</p>
          <p class="mb-2.5 mt-2.5 font-normal text-zinc-400">
            We've already sent an email with link to reset password
          </p>
          <div class="relative my-4">
            <div class="relative flex items-center py-1">
              <div class="grow border-t border-zinc-800"></div>
              <div class="grow border-t border-zinc-800"></div>
            </div>
          </div>
          <button
            onClick={() => navigate('/')}
            className='whitespace-nowrap ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 bg-white text-zinc-950 hover:bg-white/90 active:bg-white/80 flex w-full max-w-full mt-6 items-center justify-center rounded-lg px-4 py-4 text-base font-medium'
          >
            Main page
          </button>
        </div>
      </div>
    </div>
  );
};

export default ResetPasswordDone;
