import { helpers } from '@vuelidate/validators'

/**
 * Password regex - high? level
 * - At least one upper case English letter, (?=.*?[A-Z])
 * - At least one lower case English letter, (?=.*?[a-z])
 * - At least one digit, (?=.*?[0-9])
 * - At least one special character, (?=.*?[#?!@$%^&*-])
 * - Minimum eight in length .{8,} (with the anchors)
 */
export const passwordRegexHigh = helpers.regex(/^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$/)

/**
 * Password regex - medium? level
 * - At least one any case English letter, (?=.*?[A-Za-z])
 * - At least one digit, (?=.*?[0-9])
 * - Minimum eight in length .{8,} (with the anchors)
 */
export const passwordRegexMedium = helpers.regex(/^(?=.*?[A-Za-z])(?=.*?[0-9]).{8,}$/)
