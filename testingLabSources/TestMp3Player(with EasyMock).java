/**
 * Excerpted from the book, "Pragmatic Unit Testing"
 * ISBN 0-9745140-1-2
 * Copyright 2003 The Pragmatic Programmers, LLC.  All Rights Reserved.
 * Visit www.PragmaticProgrammer.com
 */

import junit.framework.*;
import java.util.ArrayList;
import static org.easymock.EasyMock.*;

public class TestMp3Player extends TestCase {

  protected Mp3Player mp3;
  protected Mp3Player mp3_control;
  protected ArrayList list = new ArrayList();

  public void setUp() {
    mp3_control = createMock(Mp3Player.class);
    mp3 = mp3_control;

    list = new ArrayList();
    list.add("Bill Chase -- Open Up Wide");
    list.add("Jethro Tull -- Locomotive Breath");
    list.add("The Boomtown Rats -- Monday");
    list.add("Carl Orff -- O Fortuna");
  }

  public void testPlay() {
    
    expect(Mp3Player.loadSongs(list));
    expect(Mp3Player.isPlaying()).andReturn(false);
    expect(Mp3Player.play());
    expect(Mp3Player.isPlaying()).andReturn(true);
    expect(Mp3Player.currentPosition()).andReturn(0.5);
    expect(Mp3Player.pause());
    expect(Mp3Player.currentPosition()).andReturn(0.5);
    expect(Mp3Player.stop());
    expect(Mp3Player.currentPosition()).andReturn(0);


    replay(mp3_control);

    mp3.loadSongs(list);
    assertFalse(mp3.isPlaying());
    mp3.play();
    assertTrue(mp3.isPlaying());
    assertTrue(mp3.currentPosition() != 0.0);
    mp3.pause();
    assertTrue(mp3.currentPosition() != 0.0);
    mp3.stop();
    assertEquals(mp3.currentPosition(), 0.0, 0.1);

  }

  public void testPlayNoList() {

    // Don't set the list up
    
    expect(Mp3Player.isPlaying()).andReturn(false);
    expect(Mp3Player.play());
    expect(Mp3Player.isPlaying()).andReturn(false);
    expect(Mp3Player.currentPosition()).andReturn(0.0);
    expect(Mp3Player.pause());
    expect(Mp3Player.currentPosition()).andReturn(0.0);
    expect(Mp3Player.isPlaying()).andReturn(false);
    expect(Mp3Player.stop());
    expect(Mp3Player.currentPosition()).andReturn(0.0);
    expect(Mp3Player.isPlaying()).andReturn(false);

    replay(mp3_control);

    assertFalse(mp3.isPlaying());
    mp3.play();
    assertFalse(mp3.isPlaying());
    assertEquals(mp3.currentPosition(), 0.0, 0.1);
    mp3.pause();
    assertEquals(mp3.currentPosition(), 0.0, 0.1);
    assertFalse(mp3.isPlaying());
    mp3.stop();
    assertEquals(mp3.currentPosition(), 0.0, 0.1);
    assertFalse(mp3.isPlaying());
  }

  public void testAdvance() {

    expect(Mp3Player.loadSongs(list));
    expect(Mp3Player.play());
    expect(Mp3Player.isPlaying()).andReturn(true);
    expect(Mp3Player.prev());
    expect(Mp3Player.currentSong()).andReturn(list.get(0));
    expect(Mp3Player.isPlaying()).andReturn(true);
    expect(Mp3Player.next());
    expect(Mp3Player.currentSong()).andReturn(list.get(1));
    expect(Mp3Player.next());
    expect(Mp3Player.currentSong()).andReturn(list.get(2));
    expect(Mp3Player.prev());
    expect(Mp3Player.currentSong()).andReturn(list.get(1));
    expect(Mp3Player.next());
    expect(Mp3Player.currentSong()).andReturn(list.get(2));
    expect(Mp3Player.next());
    expect(Mp3Player.currentSong()).andReturn(list.get(3));
    expect(Mp3Player.next());
    expect(Mp3Player.currentSong()).andReturn(list.get(3));
    expect(Mp3Player.isPlaying()).andReturn(true);

    replay(mp3_control);

    mp3.loadSongs(list);
    mp3.play();

    assertTrue(mp3.isPlaying());

    mp3.prev();
    assertEquals(mp3.currentSong(), list.get(0));
    assertTrue(mp3.isPlaying());

    mp3.next();
    assertEquals(mp3.currentSong(), list.get(1));
    mp3.next();
    assertEquals(mp3.currentSong(), list.get(2));
    mp3.prev();

    assertEquals(mp3.currentSong(), list.get(1));
    mp3.next();
    assertEquals(mp3.currentSong(), list.get(2));
    mp3.next();
    assertEquals(mp3.currentSong(), list.get(3));
    mp3.next();
    assertEquals(mp3.currentSong(), list.get(3));
    assertTrue(mp3.isPlaying());
  }

}
