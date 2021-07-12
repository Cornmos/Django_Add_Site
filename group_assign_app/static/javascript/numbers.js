/* Prevent mouse scroll wheel from changing number field
Code taken from https://thatstevensguy.com/programming/disable-arrows-on-number-inputs/
Christopher A. Stevens - May 13, 2016 */

jQuery(document).ready( function($) {

    // Disable scroll when focused on a number input.
    $('form').on('focus', 'input[type=number]', function(e) {
        $(this).on('wheel', function(e) {
            e.preventDefault();
        });
    });

    // Restore scroll on number inputs.
    $('form').on('blur', 'input[type=number]', function(e) {
        $(this).off('wheel');
    });

    // Disable up and down keys.
    $('form').on('keydown', 'input[type=number]', function(e) {
        if ( e.which == 38 || e.which == 40 )
            e.preventDefault();
    });

});
