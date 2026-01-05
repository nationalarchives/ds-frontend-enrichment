const path = require("path");
const glob = require("glob");

const dynamicEntries = glob
  .sync("./src/scripts/+(logo-adornments)/*.js")
  .reduce(
    (x, y) =>
      Object.assign(x, {
        [y.replace(/\.js$/, "").split("/").slice(-2).join("/")]: `./${y}`,
      }),
    {},
  );

module.exports = {
  entry: {
    main: "./src/scripts/main.js",
    analytics: "./src/scripts/analytics.js",
    ...dynamicEntries,
  },
  mode: "production",
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /(node_modules|bower_components)/,
        use: {
          loader: "babel-loader",
          options: {
            presets: ["@babel/preset-env"],
          },
        },
      },
    ],
  },
  output: {
    path: path.resolve(__dirname, "app/static"),
    filename: "[name].min.js",
  },
  devtool: "source-map",
};
