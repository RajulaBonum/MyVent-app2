// webpack.config.js
const path = require('path');

module.exports = {
    entry: './static/src/index.js',  // Your main JavaScript file
    output: {
        path: path.resolve(__dirname, 'static/dist'),
        filename: 'bundle.js',
    },
    module: {
        rules: [
            {
                test: /\.css$/,
                use: ['style-loader', 'css-loader'],  // For CSS files
            },
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader',  // For transpiling JavaScript
                    options: {
                        presets: ['@babel/preset-env'],
                    },
                },
            },
        ],
    },
    mode: 'development',
};
