import java.util.*;
import java.awt.Point;

class Player {
    private static Point[] site;
    private static int leftX;
    private static int rightX;
    private static int siteY;
    private static Point lander;
    private static int myR = 0;
    private static int myP = 0;

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        Point[] surface = new Point[N];
        for (int i = 0; i < N; i++) {
            int LAND_X = in.nextInt();
            int LAND_Y = in.nextInt();
            surface[i] = new Point(LAND_X, LAND_Y);
        }
        site = getSite(surface);
        leftX = (int)site[0].getX();
        rightX = (int)site[1].getX();
        siteY = (int)site[0].getY();

        int myP = 0;
        while (true) {
            int X = in.nextInt();
            int Y = in.nextInt();
            int HS = in.nextInt();
            int VS = in.nextInt();
            int F = in.nextInt();
            int R = in.nextInt();
            int P = in.nextInt();
            lander = new Point(X, Y);
            
            myR = getRotation(R, VS, HS);
            myP = getPower(R, VS, HS);
            System.out.println(msg(myR, myP));
        }
    }

    private static int getRotation (int R, int VS, int HS) {
        int X = (int)lander.getX();
        int Y = (int)lander.getY();
        int angleXcomp = 0;
        int angleHScomp = 0;
        int angle = 0;

        if (shouldKeepAltitude(X, Y) && HS != 0) {
            angle = 0;
        } else {
            angleXcomp = (int)Math.round(getDistance(X) * (3 / 185.0));
            angleXcomp += (int)(angleXcomp / 0.67);
            if (Math.abs(HS) > 7 && Y > siteY + 100) {
                angleHScomp = (int)Math.round(HS * (9 / 24.7));
                angleHScomp += (int)(angleHScomp / 0.7);
            } else {
                angleHScomp = 0;
            }
            angle = angleXcomp + angleHScomp;
            if (angle > 90 || angle < -90) {
                angle = angle > 90 ? 90 : -90;
            }
        }
        return angle;
    }

    private static int getPower(int R, int VS, int HS) {
        int X = (int)lander.getX();
        int Y = (int)lander.getY();
        int pow = 0;
        int HScomp = 0;
        int VScomp = 0;
        if (shouldKeepAltitude(X, Y) && VS < -1) {
            pow = 4;
        } else {
            if ((R < 0 && HS < 0) || (R > 0 && HS > 0)) {
                HScomp = Math.abs((int)Math.round(HS / 15.0));
            } else {
                HScomp = 0;
            }
            VScomp = -(int)Math.round(VS / 6.6);
            pow = Math.min(HScomp + VScomp, 4);
        }
        if (getDistance(X) == 0 && R == 0 && (Y - siteY) < 123 && VS > -30) {
            pow = 0;
        }
        return pow;
    }

    private static boolean shouldKeepAltitude(int X, int Y) {
        return ((Y - siteY) < 600 && getDistance(X) > 1200) ? true : false;
    }

    private static int getDistance(int X) {
        int dist = 0;
        if (X < leftX) {
            dist = X - leftX;
        } else if (X >= leftX && X <= rightX) {
            dist = 0;
        } else {
            dist = X - rightX;
        }
        return dist;
    }

    private static Point[] getSite(Point[] surface) {
        Point[] ret = new Point[2];
        for (int i = 0; i < surface.length - 1; ++i) {
            if (surface[i].getY() == surface[i + 1].getY()) {
                ret[0] = new Point(surface[i]);
                ret[1] = new Point(surface[i + 1]);
                break;
            }
        }
        return ret;
    }

    private static String msg(int R, int P) { return R + " " + P; }

    private static void debug(String s) { System.err.println(s); }
}