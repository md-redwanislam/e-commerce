const Maintenance = () => {
  return (
    <div className="min-h-screen flex items-center justify-center bg-slate-50 px-6">
      <div className="max-w-xl text-center">
        <div className="mb-6 text-7xl">🛠️</div>

        <h1 className="text-4xl md:text-5xl font-bold text-slate-800 mb-5">
          Under Maintenance
        </h1>

        <p className="text-lg text-slate-600 leading-relaxed mb-4">
          We're currently working on improving our website. We'll be back soon
          with a better experience.
        </p>

        <p className="text-sm text-slate-500">
          Thank you for your patience and understanding.
        </p>
      </div>
    </div>
  );
};

export default Maintenance;
