$(document).ready(function () {
    let tank = {};

    tank.move = function () {
        let $img = $(this);
        let direction = $img.data('direction');

        sendRequest(null, 'command/' + direction, 'get', function () {

        });
    };
    tank.stop = function () {
        sendRequest(null, 'command/stop', 'get', function () {

        });
    };

    $('.arrow-move').on('mousedown', tank.move);
    $('.arrow-move').on('mouseup', tank.stop);
});