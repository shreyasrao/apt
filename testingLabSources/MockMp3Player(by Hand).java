import java.util.ArrayList;

public class MockMp3Player implements Mp3Player{
	protected ArrayList list = new ArrayList();
	boolean isPlaying = false;
	Double currentPosition = 0.0;
	public Integer songIndex = 0;
	
	
	@Override
	public void play() {
		// TODO Auto-generated method stub
		if(list.size()==0) return;
		isPlaying = true;
		currentPosition += 0.5;
	}

	@Override
	public void pause() {
		// TODO Auto-generated method stub
		if(list.size()==0) return;
		isPlaying = false;
	}

	@Override
	public void stop() {
		// TODO Auto-generated method stub
		if(list.size()==0) return;
		currentPosition = 0.0;
	}

	@Override
	public double currentPosition() {
		// TODO Auto-generated method stub
		return currentPosition;
	}

	@Override
	public String currentSong() {
		// TODO Auto-generated method stub
		if(list.size()==0) return null;
		return (String) list.get(songIndex);
	}

	@Override
	public void next() {
		// TODO Auto-generated method stub
		if(list.size()==0) return;
		if(songIndex == list.size()-1) return;
//		System.out.println(songIndex);
		songIndex++;
	}

	@Override
	public void prev() {
		// TODO Auto-generated method stub
		if(list.size()==0) return;
		if(songIndex == 0) return;
		songIndex--;
	}

	@Override
	public boolean isPlaying() {
		// TODO Auto-generated method stub
		return isPlaying;
	}

	@Override
	public void loadSongs(ArrayList names) {
		// TODO Auto-generated method stub
		list = new ArrayList(names);
	}
	
}